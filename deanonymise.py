from mrjob.job import MRJob
import json


class MRDeAnonymise(MRJob):
    def mapper_init(self):
        self.cksum_number_map = json.load(open('rainbow.json'))

    def mapper(self, _, line):
        data = line.split(',')
        yield (','.join(map(str,
                            [self.cksum_number_map.get(data[0], 'UNKNOWN'),
                             self.cksum_number_map.get(data[1], 'UNKNOWN')] + data[2:]
                            )), None)

    def combiner(self, key, value):
        yield (key, None)

    def reducer(self, key, value):
        yield (key, None)


if __name__ == '__main__':
    MRDeAnonymise.run()
