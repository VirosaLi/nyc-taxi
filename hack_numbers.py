from mrjob.job import MRJob
import json


class MRHackLicences(MRJob):
    def mapper_init(self):
        self.cksum_number_map = json.load(open('rainbow.json'))

    def mapper(self, _, line):
        data = line.split(',')
        hack_no = self.cksum_number_map.get(data[1], 'UNKNOWN')
        yield (str(hack_no), 1)

    def combiner(self, key, value):
        yield (key, sum(value))

    def reducer(self, key, value):
        yield (key, sum(value))


if __name__ == '__main__':
    MRHackLicences.run()
