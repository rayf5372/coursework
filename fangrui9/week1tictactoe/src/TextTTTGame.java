import entity.TicTacToeBoard;
import usecase.MakeMoveUseCase;
import adapter.TicTacToePresenter;
import adapter.TicTacToeController;
import view.TicTacToeView;
import view.TicTacToeCLIView;

import java.util.Scanner;

public class TextTTTGame {
    public static void main(String[] args) {
        TicTacToeBoard board = new TicTacToeBoard();
        TicTacToeView view = new TicTacToeCLIView();
        TicTacToePresenter presenter = new TicTacToePresenter(view);
        MakeMoveUseCase useCase = new MakeMoveUseCase(board, presenter);
        TicTacToeController controller = new TicTacToeController(useCase);
        Scanner scanner = new Scanner(System.in);

        System.out.println("To exit the game at any time, type '9'. To start, type any other number.");
        int userCommand = scanner.nextInt();

        while (userCommand != 9) {
            view.displayBoard(board.getBoard());
            System.out.println("Player " + board.getCurrentPlayer() + ", enter your move by typing the row then a space then column number. Your options are 0, 1, or 2.");

            int row = scanner.nextInt();
            /*
            TODO 1 line
            There's a variable declaration missing. Its initial value should come from the scanner.
             */
            int col = scanner.nextInt();

            controller.makeMove(row, col);
            if (board.checkWin() != '-' || board.isFull()) {
                break;
            }
            userCommand = row;
        }

        view.displayBoard(board.getBoard());
        char winner = board.checkWin();
        if (winner != '-') {
            view.displayWinner(winner);
        } else {
            view.displayWinner('D'); // Draw
        }
    }
}
