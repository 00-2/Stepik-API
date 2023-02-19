from library.models import ItemReport

class ContestTable():

    _step_submissions = []
    _contesters = dict()
    def __init__(self, course_id):
        self.report = ItemReport(course_id)
        self.report.course_id = course_id
    def get_step_submissions(self):
        self._step_submissions = self.report.build()
        return self._step_submissions
    def get_contesters(self):
        if self._step_submissions == []:
            self.get_step_submissions(self)
        for i, step in enumerate(self._step_submissions):
            for costentant in step.index.values.tolist():
                if i > 1:
                    try:
                        score = step.loc[costentant]['score']
                        self._contesters[costentant] += score
                    except KeyError:
                        self._contesters[costentant] = 0
                else:
                    self._contesters[costentant] = 0

        self._contesters = sorted(self._contesters.items(), key=lambda x: -x[1])
        return self._contesters