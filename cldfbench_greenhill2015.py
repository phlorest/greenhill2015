import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "greenhill2015"

    def cmd_makecldf(self, args):
        self.init(args)
        args.writer.add_summary(
            self.raw_dir.read_tree(
                'mcelhanon-1967-covarion.mcct.trees', detranslate=True),
            self.metadata,
            args.log)
        
        posterior = self.sample(
            self.remove_burnin(
                self.raw_dir.read('mcelhanon-1967-covarion.trees.gz'),
                10001),
            detranslate=True,
            as_nexus=True)
        args.writer.add_posterior(
            posterior.trees.trees,
            self.metadata,
            args.log)

        args.writer.add_data(
            self.raw_dir.read_nexus('mcelhanon-1967.nex'),
            self.characters,  # no characters
            args.log)