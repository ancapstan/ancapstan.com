import nox


@nox.session
def tests(session):
    session.install('-r', 'requirements.txt')
    session.run('nikola', 'build', '--strict')


@nox.session
def lint_rst(session):
    session.install('rstcheck')
    session.run('rstcheck', '-r', '.')
