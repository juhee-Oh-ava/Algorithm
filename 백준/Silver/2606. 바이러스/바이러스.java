import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static int[][] node;
    public static boolean[] visited;
    public static int N, conn;
    public static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        conn = Integer.parseInt(br.readLine());

        node = new int[N+1][N+1];
        visited = new boolean[N+1];

        for (int i = 0; i < conn; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            node[a][b] = node[b][a] = 1;
        }

        dfs(1);
        System.out.println(result);
    }

    public static void dfs(int x){
        visited[x] = true;

        for (int i = 1; i <= N; i++){
            if (node[x][i] == 1 && !visited[i]){
                result++;
                dfs(i);
            }
        }
    }
}
