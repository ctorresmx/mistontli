#! /usr/bin/env python
import fire
import mistontli


class Mistontli:
    def start_game(self):
        print('Welcome to Mistontli!')


if __name__ == '__main__':
    fire.Fire(mistontli.Mistontli)
