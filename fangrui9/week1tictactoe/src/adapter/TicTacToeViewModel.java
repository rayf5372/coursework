package adapter;

public class TicTacToeViewModel {
    private final char[][] board;
    private final char winner;
    private final String errorMessage;

    public TicTacToeViewModel(char[][] board, char winner, String errorMessage) {
        this.board = board;
        this.winner = winner;
        this.errorMessage = errorMessage;
    }

    public char[][] getBoard() {
        return board;
    }

    public char getWinner() {
        return winner;
    }

    public String getErrorMessage() {
        return errorMessage;
    }
}