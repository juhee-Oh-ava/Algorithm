import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<Integer>[] graph;
    static int[] visited;
    static ArrayList<Integer> procedure;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        visited = new int[N + 1];
        procedure = new ArrayList<>();
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        for (int i = 1; i < N+1; i++){
            if (visited[i] != 1) {
                count++;
                DFS(i);

            }
        }


//        System.out.println(Arrays.toString(graph));
        System.out.println(count);

    }

    static void DFS(int v) {
        if (visited[v] == 1) {
            return;
        }

        visited[v] = 1;
        procedure.add(v);

        for (int i : graph[v]) {
            if (visited[i] != 1) {
                DFS(i);
            }
        }

    }
}

