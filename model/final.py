class FinalModel:
    Name ='' #project name. Only info variable
    Year = 0 #start year of project, 2018 for example. Only info variable
    Duration=0 #real duration in months for model's validation

    #Below variables are inputs
    Platform =0 #0 - Generic, 1 - Web, 2 - Mobile, 3 - Desktop
    Language =0  # 0 - Generic, 1 - Js, 2 - Go, 3 - Python, 4 - Java-like, 5 - C#, 6 - C++, 7 - C, 8 - PHP, 9 - Delphi/Pascal
    #project team
    #rank: 1-junior, 3-middle, 5-senior
    #time mode: 1 - fulltime (8 hours/work day), 0.125 - parttime 1 hour/work day, i.e
    #team=sum (rank_i*time_i)
    #example - 1 fulltime junior and 1 parttime (4 hour) seniour: team=1*1+5*0.5=3.5
    Team=0.0
    SizeMetric=0 #Unknown - 0, KLOC - 1
    Size=0 #size in {SizeMetric} units
    DevelopmentMode=0 #0 - new project, 1 - rework
    CodeReuse=0.0 # - code reuse part (from 0 to 1.0)
    Architecture=0 #0 - generic, 1 - level, 2 - monolith, 3 - microservices
    CustomerQuality=0 #1 - low, 2 - middle, 3 - high
    ProjectManagementQuality=0 #1 - low, 2 - good, 3 - high

    def __iter__(self):
        return iter([self.Name,
                     self.Year,
                     self.Platform,
                     self.Language,
                     self.Team,
                     self.SizeMetric,
                     self.Size,
                     self.DevelopmentMode,
                     self.CodeReuse,
                     self.Architecture,
                     self.CustomerQuality,
                     self.ProjectManagementQuality,
                     self.Duration
                     ])
    def getColumns (self):
        return ['Name',
                'Year',
                'Platform',
                'Language',
                'Team',
                'SizeMetric',
                'Size',
                'DevelopmentMode',
                'CodeReuse',
                'Architecture',
                'CustomerQuality',
                'ProjectManagementQuality',
                'Duration']

    def toArr4(self):
        return iter([self.Name,
                     self.Year,
                     self.Platform,
                     self.Team,
                     self.Size,
                     self.CodeReuse,
                     self.CustomerQuality,
                     self.ProjectManagementQuality,
                     self.Duration
                     ])

    def getColumns4 (self):
        return ['Name',
                'Year',
                'Platform',
                'Team',
                'Size',
                'CodeReuse',
                'CustomerQuality',
                'ProjectManagementQuality',
                'Duration']

    def toArr3(self):
        return iter([self.Name,
                     self.Year,
                     self.Platform,
                     self.Language,
                     self.Team,
                     self.Size,
                     self.CodeReuse,
                     self.Architecture,
                     self.CustomerQuality,
                     self.ProjectManagementQuality,
                     self.Duration
                     ])

    def getColumns3 (self):
        return ['Name',
                'Year',
                'Platform',
                'Language',
                'Team',
                'Size',
                'CodeReuse',
                'Architecture',
                'CustomerQuality',
                'ProjectManagementQuality',
                'Duration']