class Diff(object):
    def __init__(self, ratio=1):
        if not isinstance(ratio, (int, float)):
            raise ExamExecption('Invalid ratio.')
        self.ratio = ratio

    def compute(self, lista):
        if lista is None:
            raise ExamExecption('Data dne.')
        if not type(lista) is list:
            raise ExamExecption(f'List type expected. found {type(lista)}.')
        if len(lista) == 0:
            raise ExamExecption('Empty list.')
        result = []
        for i in range(1, len(lista)):
            if not isinstance(lista[i], (int, float)):
                raise ExamExecption('Invalid value.')
            if not isinstance(lista[i-1], (int, float)):
                raise ExamExecption('Invalid value.')
            curr = (lista[i] - lista[i-1]) / self.ratio
            result.append(curr)
        return result


class ExamExecption(Exception):
    pass
