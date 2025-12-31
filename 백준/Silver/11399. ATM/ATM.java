import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        ArrayList<Integer> lst = new ArrayList<>();

        String[] input = br.readLine().split(" ");

        for (int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(input[i]);
        }

//        System.out.println(Arrays.toString(arr));

        Arrays.sort(arr);
        int sum_v = 0;
        for (int i = 0; i < N; i++){
            sum_v += arr[i];
            lst.add(sum_v);
        }

        int result = 0;
        for (int k : lst){
            result += k;
        }

        System.out.println(result);
    }
}
