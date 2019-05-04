import subprocess
import sys
import pytest
import rsp_lib
import rsp


def test_rock_is_valid_input():
    result = rsp_lib.is_valid_choice("rock")
    assert result


def test_paper_is_valid_input():
    result = rsp_lib.is_valid_choice("paper")
    assert result


def test_scissors_is_valid_input():
    result = rsp_lib.is_valid_choice("scissors")
    assert result


def test_spock_isnot_valid_input():
    result = rsp_lib.is_valid_choice("spock")
    assert not result


def test_lizard_isnot_valid_input():
    result = rsp_lib.is_valid_choice("lizard")
    assert not result


def test_random_play():
    """
    Stokrat udelame nahodny vyber. assert na count neni stastny vyhodi nam
    assert i kdyz to funguje
    """
    AI_choices = [rsp_lib.random_choice() for _ in range(100)]
    # podtrzitko ve foru rika pythonu ze tuto promennou nebudu potrebova
    # (nebudu pouzivat prommenou) mohu tam dat normalne promennou ale spravny
    # programator to nedela
    # protoze zbytecne alokujeme v pc pamet pro promennou kterou nepouzivame

    assert AI_choices.count("rock") > 10
    assert AI_choices.count("scissors") > 10
    assert AI_choices.count("paper") > 10

    for choice in AI_choices:
        assert rsp_lib.is_valid_choice(choice)


@pytest.mark.parametrize("player, computer", [("rock", "scissors"),
                                              ("scissors", "paper"),
                                              ("paper", "rock")])
def test_get_game_results_when_player_wins(player, computer):
    # parametricky test @ je dekodator - spusti se pred testovaci funkci
    # a funkci rekne divej pouzij tohle co jsem vytvoril
    assert rsp_lib.get_game_results(player, computer) == 1


@pytest.mark.parametrize("player, computer", [("rock", "scissors"),
                                              ("scissors", "paper"),
                                              ("paper", "rock")])
def test_get_game_results_when_computer_wins(computer, player):
    # parametricky test pomoci @pytest.mark.parametrize
    assert rsp_lib.get_game_results(computer, player) == -1


@pytest.mark.parametrize("player, computer", [("rock", "rock"),
                                              ("scissors", "scissors"),
                                              ("paper", "paper")])
def test_get_game_results_when_is_tie(player, computer):
    # parametricky test
    assert rsp_lib.get_game_results(player, computer) == 0


def test_print(capsys):
    # fixture (treba capsys) moznost jak delat s testovacimi funkcemi
    print("Hello world !")

    captured = capsys.readouterr()
    assert "Hello" in captured.out


def fake_input(promt):
    """
    pomocna funkce ktera nahrazuje input, promt je parametr inputu
    """
    print(promt)
    return "Rock"


def fake_random_choice(list_choices):
    """
    random choice si nastavime aby nam vracel hdnotu kterou potrebujemr
    a ne nahodne
    """
    return "paper"


def test_full_game_printing(capsys, monkeypatch):
    """
    test ktery kontroluej printy
    integrační test - problem s inputem test ceka na input
    monkey patching nahrazeni inputu nasi vytvorenou nasi funkci
    builtins je modul v kterem se nachazi input
    bez do vstupu input a nahrad ji nasi funkci fake_input

    pokud mame IMPORT RANDOM potom piseme
    monkeypatch.setattr("random.choice", fake_random_choice)
    Duvod: importujeme cely modul random a cesta je random.choice

    pokud mame FROM RANDOM IMPORT CHOICE potom piseme
    monkeypatch.setattr("rsp.choice", fake_random_choice)
    Duvod: choice importujeme pouze do sveho souboru a exituje jen v nasem
    souboru cesta k nemu je tedy pres nazev souboru rsp.choice
    """

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr("rsp.choice", fake_random_choice)
    rsp.main()

    captured = capsys.readouterr()
    assert "Rock, Paper or Scissors:" in captured.out
    assert "Player choiced: rock" in captured.out
    assert "Computer choiced: paper" in captured.out
    assert "Player lost !" in captured.out


def test_play_game():
    """
    subprocess.run - simuluje zapnuti program ujako by to udelal clovek za
    pocitacem.
    sys.executable - spust soubor rsp.py jako python soubor
    input - pokud bude chtit program input tak dej asdd potom enter =\n
    potom zadej znova rock.

    encoding se pouziva protoze kazdy prikazovy radek ma jinou sadu

    stdout = (out) - vystup, nevypisuj na obrazovku ale hod to do
    subprocess.PIPE z neho si to potom kdyz tak vytahnem
    """
    p = subprocess.run([sys.executable, "rsp.py"],
                       input="asdd\nrock",
                       encoding="utf-8",
                       stdout=subprocess.PIPE)
    assert p.stdout.count("Rock, Paper or Scissors:") == 2
