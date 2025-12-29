import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static boolean[][] visited;
    static int[][] arr;
    static int count;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, -1, 0, 1};
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        N = Integer.parseInt(str);
        arr = new int[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++){
            String line = br.readLine();
            for (int j = 0; j < N; j++){
                arr[i][j] = line.charAt(j) - '0';
            }
        }

        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i < N; i++){
            for (int j = 0; j < N; j++){
                if (arr[i][j] == 1 && !visited[i][j]){
                    count = 0;
                    bfs(i, j);
                    result.add(count);
                }
            }
        }
        
        System.out.println(result.size());
        Collections.sort(result);
        for (int x : result) System.out.println(x);


    }
    static void bfs(int r, int c){
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;

        while(!q.isEmpty()){
            int[] cur = q.poll();
            count++;
            int cr = cur[0];
            int cc = cur[1];

            for (int d = 0; d < 4; d++){
                int nr = cr + dr[d];
                int nc = cc + dc[d];

                if (0 <= nr && nr < N && 0 <= nc && nc < N){
                    if (arr[nr][nc] == 1 && !visited[nr][nc]){
                        q.add(new int[] {nr, nc});
                        visited[nr][nc] = true;
                    }
                }

            }
        }
    }
}
