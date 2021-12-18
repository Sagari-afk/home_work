class CalculatorUtil:
    status_on = 'on'
    status_off = 'off'

    common_calc = 'common'
    graphs_calc = 'gra'
    scientific_calc = 'sci'

    @classmethod
    def statuses(cls):
        return (cls.status_on, cls.status_off)

    @classmethod
    def models(cls):
        return cls.common_calc, cls.graphs_calc, cls.scientific_calc