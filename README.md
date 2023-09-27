## Features

* Detects vulnerable Solidity code with low false positives (see the list of [trophies](./trophies.md))
* Identifies where the error condition occurs in the source code
* Easily integrates into continuous integration and Hardhat/Foundry builds
* Built-in 'printers' quickly report crucial contract information
* Detector API to write custom analyses in Python
* Ability to analyze contracts written with Solidity >= 0.4
* Intermediate representation ([SlithIR](https://github.com/khulnasoft-lab/solscan/wiki/SlithIR)) enables simple, high-precision analyses
* Correctly parses 99.9% of all public Solidity code
* Average execution time of less than 1 second per contract
* Integrates with Github's code scanning in [CI](https://github.com/marketplace/actions/solscan-action)

## Usage

Run Solscan on a Hardhat/Foundry/Dapp/Brownie application:

```console
solscan .
```

This is the preferred option if your project has dependencies as Solscan relies on the underlying compilation framework to compile source code.

However, you can run Solscan on a single file that does not import dependencies:

```console
solscan tests/uninitialized.sol
```

## How to install

> **Note** <br />
> Solscan requires Python 3.8+.
If you're **not** going to use one of the [supported compilation frameworks](https://github.com/crytic/crytic-compile), you need [solc](https://github.com/ethereum/solidity/), the Solidity compiler; we recommend using [solc-select](https://github.com/crytic/solc-select) to conveniently switch between solc versions.

### Using Pip

```console
pip3 install solscan-analyzer
```

### Using Git

```bash
git clone https://github.com/crytic/solscan.git && cd solscan
python3 setup.py install
```

We recommend using a Python virtual environment, as detailed in the [Developer Installation Instructions](https://github.com/khulnasoft-lab/solscan/wiki/Developer-installation), if you prefer to install Solscan via git.

### Using Docker

Use the [`eth-security-toolbox`](https://github.com/khulnasoft-lab/eth-security-toolbox/) docker image. It includes all of our security tools and every major version of Solidity in a single image. `/home/share` will be mounted to `/share` in the container.

```bash
docker pull khulnasoft-lab/eth-security-toolbox
```

To share a directory in the container:

```bash
docker run -it -v /home/share:/share khulnasoft-lab/eth-security-toolbox
```

### Integration

* For GitHub action integration, use [solscan-action](https://github.com/marketplace/actions/solscan-action).
* To generate a Markdown report, use `solscan [target] --checklist`.
* To generate a Markdown with GitHub source code highlighting, use `solscan [target] --checklist --markdown-root https://github.com/ORG/REPO/blob/COMMIT/` (replace `ORG`, `REPO`, `COMMIT`)
