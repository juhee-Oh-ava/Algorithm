import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int N, v1, c1, v2, c2;
    static int[][] board;
    static boolean[][] visited;
    static int[] dr = {-2, -2, 0, 0, 2, 2};
    static int[] dc = {-1, 1, -2, 2, -1, 1};
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        v1 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        v2 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        visited = new boolean[N+1][N+1];
        board = new int[N+1][N+1];

        int result = bfs(v1, c1);
        System.out.println(result);


    }
    static int bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visited[x][y] = true;
        board[x][y] = 0; // 시작 거리

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cr = cur[0];
            int cc = cur[1];

            if (cr == v2 && cc == c2) {
                return board[cr][cc];
            }

            for (int i = 0; i < 6; i++) {
                int nr = cr + dr[i];
                int nc = cc + dc[i];

                if (0 <= nr && nr <= N && 0 <= nc && nc <= N) {
                    if (!visited[nr][nc]) {
                        visited[nr][nc] = true;
                        board[nr][nc] = board[cr][cc] + 1;
                        q.offer(new int[]{nr, nc});
                    }
                }
            }


        }
        return -1;

    }


    }
