public class SudokuSolver {

    private static final int GRID_SIZE = 9;
    public static void main(String[] args){
        int[][] board = {
            {7,0,2,0,5,0,6,0,0},
            {0,0,0,0,0,3,0,0,0},
            {1,0,0,0,0,9,5,0,0},
            {8,0,0,0,0,0,0,9,0},
            {0,4,3,0,0,0,7,5,0},
            {0,9,0,0,0,0,0,0,8},
            {0,0,9,7,0,0,0,0,5},
            {0,0,0,2,0,0,0,0,0},
            {0,0,7,0,4,0,2,0,3}
        };

        if(solve_board(board)){
            System.out.println("solved successfully");
        } else {
            System.out.println("Unsolveable board :(");
        }
        print_board(board);
    }
    private static void print_board(int[][] board){
        for(int row = 0; row < GRID_SIZE; row++){
            if(row % 3 == 0 && row != 0){
                System.out.println("----------");
            }
            for(int column = 0; column < GRID_SIZE; column++){
                if(column % 3 == 0 && column != 0){
                    System.out.print("|");
                }
                System.out.print(board[row][column]);
            }
            System.out.println();
        }
    }

    private static boolean is_number_in_row(int[][] board, int number, int row){
        for(int i = 0; i < GRID_SIZE; i++){
            if(board[row][i] == number){
                return true;
            }
        }
        return false;
    }

    private static boolean is_number_in_column(int[][] board, int number, int column){
        for(int i = 0; i < GRID_SIZE; i++){
            if(board[i][column] == number){
                return true;
            }
        }
        return false;
    }

    private static boolean is_number_in_box(int[][] board, int number, int row, int column){
        int local_box_row = row - row % 3;
        int local_box_column = column - column % 3;

        for(int i = local_box_row; i < local_box_row + 3; i ++){
            for(int j = local_box_column; j < local_box_column; j++){
                if(board[i][j] == number){
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean is_valid_placement(int[][] board, int number, int row, int column){
        return (!is_number_in_row(board, number, row) &&
        !is_number_in_column(board, number, column) &&
        !is_number_in_box(board, number, row, column));
    }

    private static boolean solve_board(int[][] board){
        for(int row = 0; row < GRID_SIZE; row++){
            for(int column = 0; column < GRID_SIZE; column++){
                if(board[row][column] == 0){
                    for(int number_to_try = 1; number_to_try <= GRID_SIZE; number_to_try++){
                        if(is_valid_placement(board, number_to_try, row, column)){
                            board[row][column] = number_to_try;

                            if(solve_board(board)){
                                return true;
                            } else {
                                board[row][column] = 0;
                            }
                        }
                    }
                return false;
                }
            }
        }
        return true;
    }
}