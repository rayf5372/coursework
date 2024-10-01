package usecase;

public interface MakeMoveOutputBoundary {
    void presentBoard(char[][] board);
    void presentWinner(char winner);
    void presentError(String message);
}