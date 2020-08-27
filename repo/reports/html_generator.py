class HTMLGenerator():
    @classmethod
    def build(cls, repos):
        items = ' '.join(
            f'<strong>ID: </strong>{repo.id} <strong>name: </strong>{repo.name} <strong>stars: </strong>{repo.stars}\n'
            for repo in repos)
        return f'<p>{items}</p>'
