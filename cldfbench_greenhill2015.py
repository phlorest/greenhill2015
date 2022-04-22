import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "greenhill2015"

    def cmd_makecldf(self, args):
        self.init(args)
        
        summary = self.raw_dir.read_tree(
            'mcelhanon-1967-covarion.mcct.trees', detranslate=True)
        args.writer.add_summary(summary, self.metadata, args.log)

        posterior = self.raw_dir.read_trees(
           'mcelhanon-1967-covarion.trees.gz',
           burnin=10001, sample=1000, detranslate=True)
        args.writer.add_posterior(posterior, self.metadata, args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('mcelhanon-1967.nex'),
            self.characters,  # no characters
            args.log)