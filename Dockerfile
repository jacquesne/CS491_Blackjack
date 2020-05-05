FROM python:3
ADD main.py /
ADD dealer.py /
ADD deck.py /
ADD game.py /
ADD player.py /
ADD tests.py /
CMD [ "python", "./main.py" ]