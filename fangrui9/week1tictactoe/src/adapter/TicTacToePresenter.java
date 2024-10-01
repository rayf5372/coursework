package adapter;

import usecase.MakeMoveOutputBoundary;
import view.TicTacToeView;

public class TicTacToePresenter implements MakeMoveOutputBoundary {
    private final TicTacToeView view;

    public TicTacToePresenter(TicTacToeView view) {
        this.view = view;
    }

    @Override
    public void presentBoard(char[][] board) {
        view.displayBoard(board);
    }

    @Override
    public void presentWinner(char winner) {
        view.displayWinner(winner);
    }

    @Override
    public void presentError(String message) {
        view.displayError(message);
    }
}