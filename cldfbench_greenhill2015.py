import pathlib

import phlorest


class Dataset(phlorest.Dataset):
    dir = pathlib.Path(__file__).parent
    id = "greenhill2015"

    def cmd_makecldf(self, args):
        """
summary.trees: original/mcelhanon-1967-covarion.mcct.trees
	cp $< $@

posterior.trees: original/mcelhanon-1967-covarion.trees.gz
	nexus trees -d 1-10001 $< -o tmp
	nexus trees -t -c -n 1000 tmp -o $@
	rm tmp

data.nex:
	cp original/mcelhanon-1967.nex $@
        """
        self.init(args)
        with self.nexus_summary() as nex:
            self.add_tree_from_nexus(
                args,
                self.raw_dir / 'mcelhanon-1967-covarion.mcct.trees',
                nex,
                'summary',
                detranslate=True,
            )
        posterior = self.sample(
            self.remove_burnin(
                self.read_gzipped_text(self.raw_dir / 'mcelhanon-1967-covarion.trees.gz'), 10001),
            detranslate=True,
            as_nexus=True)

        with self.nexus_posterior() as nex:
            for i, tree in enumerate(posterior.trees.trees, start=1):
                self.add_tree(args, tree, nex, 'posterior-{}'.format(i))

        self.add_data(args, self.raw_dir / 'mcelhanon-1967.nex')
