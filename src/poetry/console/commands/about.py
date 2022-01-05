from poetry.console.commands.command import Command


class AboutCommand(Command):

    name = "about"

    description = "Shows information about Poetry."

    def handle(self) -> None:
        self.line(
            "<info>Poetry - Package Management for Python</info>\n\n"
            "<comment>Poetry is a dependency manager tracking local dependencies "
            "of your projects and libraries.\n"
            "See <fg=blue>https://github.com/python-poetry/poetry</> "
            "for more information.</comment>"
        )
