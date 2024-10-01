package view;

public class TicTacToeCLIView implements TicTacToeView {
    @Override
    public void displayBoard(char[][] board) {
        for (char[] row : board) {
            for (char cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }

    @Override
    public void displayWinner(char winner) {
        if (winner == 'D') {
            System.out.println("The game is a draw.");
        } else {
            System.out.println("Player " + winner + " wins!");
        }
    }

    @Override
    public void displayError(String message) {
        System.out.println(message);
    }
}