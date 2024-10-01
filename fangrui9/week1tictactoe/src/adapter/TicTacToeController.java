package adapter;

import usecase.MakeMoveInputBoundary;

public class TicTacToeController {
    private final MakeMoveInputBoundary inputBoundary;

    public TicTacToeController(MakeMoveInputBoundary inputBoundary) {
        this.inputBoundary = inputBoundary;
    }

    public void makeMove(int row, int col) {
        inputBoundary.makeMove(row, col);
    }
}