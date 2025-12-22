import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collection;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < N; i++){
            String str = br.readLine();
            int x = Integer.parseInt(str);
            if (x > 0){
                maxHeap.add(x);
            } else if (x == 0 ) {
                if (maxHeap.isEmpty()) {
                    System.out.println(0);
                }else{
                    int p = maxHeap.poll();
                    System.out.println(p);
                }

            }

        }
    }
}
