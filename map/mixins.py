class QuickActionsMixin:
    def get_quick_actions(self):
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quick_actions'] = self.get_quick_actions()
        return context
