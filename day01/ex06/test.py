#!/usr/bin/env python3
from the_bank import Account, Bank


def main():
	peer = Account('Peer', zit=8096, value=4)
	peer.transfer(16)
	bank = Bank()
	bank.add(peer)
	bank.transfer('Peer', 'Peer', 8)
	daddy = Account('Daddy', address='RLD 8', value=0)
	bank.add(daddy)
	bank.transfer('Peer', 'Daddy', 5)


if __name__ == '__main__':
	main()
