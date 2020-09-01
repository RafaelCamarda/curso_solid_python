class HTMLGenerator():
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'<strong>ID: </strong>{repo.id} <strong>NAME: </strong>{repo.name} <strong>STARS: </strong>{repo.stars}\n'
            for repo in repos)
        return f'<p>{items}</p>'
