import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    static int N, x, y, m;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int count;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        if (x > y) {
            int temp = x;
            x = y;
            y = temp;
        }

        m = Integer.parseInt(br.readLine());

        graph = new ArrayList[N+1];
        visited = new boolean[N+1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 1; i <= N; i++) {
            Collections.sort(graph[i]);
        }

        if (DFS(x) == false) {
            System.out.println(-1);
        } else {
            System.out.println(count);
        }


    }
    static boolean DFS(int start) {
        if (start == y) {
            return true;
        }

        visited[start] = true;

        for (int ele : graph[start]) {
            if (!visited[ele]) {
                count++;
                if (DFS(ele)) return true;
                count--;
            }
        }
        return false;
        }

    }

