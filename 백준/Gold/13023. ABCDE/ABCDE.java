import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.CookieHandler;
import java.util.*;

public class Main {
    static int N, M;
    static ArrayList<Integer> [] graph;
    static boolean[] visited;
    static int count;
    static List<Integer> result;
    static int answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        visited = new boolean[N+1];
        for (int i = 0; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i = 0; i < N+1; i++) {
            Collections.sort(graph[i]);
        }


        result = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            visited = new boolean[N+1];
            count = 0;

            result.add(DFS(i));

        }


        for (int k : result) {
            if (k == 1) {
                System.out.println(1);
                break;
            } else {
                answer++;
                if (answer == result.toArray().length) {
                    System.out.println(0);
                }
            }
        }





    }
    static int DFS(int start) {
        if (count == 4) {
//            System.out.println(1);
            return 1;
        }
        visited[start] = true;

        for (int friend : graph[start]) {
            if (!visited[friend]) {
                count++;
                if (DFS(friend) == 1) {
                    return 1;
                }
                count--;
                visited[friend] = false;
            }
        }
        return 0;
    }
}
