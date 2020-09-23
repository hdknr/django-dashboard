class Topic:
    @property
    def full_code(self):
        return '/'.join(i.code for i in self.get_ancestors(include_self=True))

    @property
    def full_title(self):
        return '/'.join(i.title for i in self.get_ancestors(include_self=True))

    @property
    def full_code_path(self):
        return '/' + self.full_code

    @classmethod
    def path_info(cls, full_name):
        paths = [i for i in full_name.split('/') if i]
        return paths and (paths[-1], paths.index(paths[-1])) or ('', -1)


class Message:
    pass


class Notice:
    pass
