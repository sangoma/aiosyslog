"""Syslog server."""
import asyncio
import typing as t

import attr
from .abc import AbstractMessageLogger


class MessageLogger(AbstractMessageLogger):
    def __init__(self):
        import logging
        self.logger = logging.getLogger(__name__)

    def log(self, message, addr):
        self.logger.info(message)

    def exception(self, addr):
        self.logger.exception('Failed to parse syslog message from {}'.format(
            addr[0]))


@attr.s(auto_attribs=True)
class SyslogProtocol(asyncio.Protocol):
    """Syslog protocol support."""
    server: 'SyslogServer' = attr.ib()

    def datagram_received(self, data: bytes, addr: t.Tuple[str, int]):
        """Handle incoming package."""
        try:
            message = self.server.message_class.parse(data)
            self.server.logger.log(message, addr)
        except Exception as exc_info:
            self.server.logger.exception(exc_info, addr)


@attr.s
class SyslogServer:
    """Server to receive incoming syslog messages."""
    message_class = attr.ib()
    logger_class = attr.ib(default=MessageLogger)

    transport: asyncio.Transport = attr.ib(init=False)
    protocol: SyslogProtocol = attr.ib(init=False)
    logger = attr.ib(init=False)

    _loop: asyncio.BaseEventLoop = attr.ib(
        init=False, factory=asyncio.get_event_loop)

    @logger.default
    def get_logger(self):
        return self.logger_class()

    async def run(self, local_addr: t.Tuple[str, int] = None) -> None:
        """Start listening for incoming syslog messages."""
        connection = await self._loop.create_datagram_endpoint(
            lambda: SyslogProtocol(self),
            local_addr=local_addr or ('0.0.0.0', 514))

        self.transport, self.protocol = connection

    def close(self) -> None:
        """Close the syslog server."""
        self.transport.close()
