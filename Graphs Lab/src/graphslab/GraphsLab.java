package graphslab;

import java.util.*;

public class GraphsLab {

    public static void main(String[] args) {
        // create the primpq given in above figure
        int V = 6;
        Prim primpq = new Prim(V);

        //  making above shown primpq
        primpq.addEdge(0, 1, 2);
        primpq.addEdge(0, 3, 1);
        primpq.addEdge(0, 4, 4);
        primpq.addEdge(1, 3, 3);
        primpq.addEdge(1, 2, 3);
        primpq.addEdge(1, 5, 7);
        primpq.addEdge(3, 4, 9);
        primpq.addEdge(3, 2, 5);
        primpq.addEdge(2, 5, 8);
       

        primpq.primMST();
        System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
        //////////////////////////////////////////////////////////////////////////////
        V = 6;
        int source = 4;
        Dijkstra dpq = new Dijkstra(V);
        //Adding sublist to the adjacency array list 
        //aka Adding adjacent nodes to every node
        dpq.adj_list.get(0).add(new Node(1, 2));
                dpq.adj_list.get(1).add(new Node(0, 2));
        dpq.adj_list.get(0).add(new Node(3, 1));
         dpq.adj_list.get(3).add(new Node(0, 1));
        dpq.adj_list.get(0).add(new Node(4, 4));
        dpq.adj_list.get(4).add(new Node(0, 4));
        dpq.adj_list.get(1).add(new Node(3, 3));
        dpq.adj_list.get(3).add(new Node(1, 3));
        dpq.adj_list.get(1).add(new Node(2, 3));
        dpq.adj_list.get(2).add(new Node(1, 3));
        dpq.adj_list.get(1).add(new Node(5, 7));
        dpq.adj_list.get(3).add(new Node(4, 9));
        dpq.adj_list.get(4).add(new Node(3, 9));
        dpq.adj_list.get(3).add(new Node(2, 5));
        dpq.adj_list.get(2).add(new Node(3, 5));
        dpq.adj_list.get(2).add(new Node(5, 8));
                dpq.adj_list.get(5).add(new Node(2, 8));

        dpq.algorithm(dpq.adj_list, source);
        dpq.dijkstraSP(dpq, source);
        // Print the shortest path from source vertexLabel to all the nodes 
    }
}

class Dijkstra {

    int dist[];
    ArrayList<Integer> visited;
    PriorityQueue<Node> pqueue;
    int V; // Number of vertices 
    List<List<Node>> adj_list;

    //class constructor
    public Dijkstra(int V) {
        this.V = V;
        dist = new int[V];
        visited = new ArrayList<>();
        pqueue = new PriorityQueue<>(V, new Node());
        adj_list = new ArrayList<List<Node>>();
        //Creating the Adjacency list with all nodes and no edges yet
        for (int i = 0; i < V; i++) {
            List<Node> item = new ArrayList<Node>();
            adj_list.add(item);
        }
    }

    // Dijkstra's Algorithm implementation 
    public void algorithm(List<List<Node>> adj_list, int source) {
        this.adj_list = adj_list;

        for (int i = 0; i < V; i++) {
            dist[i] = Integer.MAX_VALUE;
            //System.out.println(i+"------>"+dist[i]);
        }

        // first add source vertex to PriorityQueue 
        pqueue.add(new Node(source, 0));

        // Distance to the source from itself is 0 
        dist[source] = 0;
        while (visited.size() != V) {
            // u is removed from PriorityQueue and has min distance  
            int u = pqueue.remove().vertexLabel;
            //System.out.println("\n");
            //System.out.println(u + "<-------------Next Node from pq");
            //System.out.println("size of queue: " + pqueue.size());

            // add vertexLabel to finalized list (visited)
            visited.add(u);
            adjacentNodes(u);

        }
    }
    // this methods processes all neighbours of the just visited vertexLabel 

    private void adjacentNodes(int u) {
        int edgeDistance = -1; //Weight of edge
        int newDistance = -1;   //Weights till the node is reached

        // process all neighbouring nodes of u 
        for (int i = 0; i < adj_list.get(u).size(); i++) {
            Node v = adj_list.get(u).get(i);
            //System.out.println("checking adj vertexLabel ---------->" + v.vertexLabel);
            //  proceed only if current vertexLabel is not in 'visited'
            if (!visited.contains(v.vertexLabel)) {
                edgeDistance = v.weight;
                newDistance = dist[u] + edgeDistance;

                // compare distances 
                if (newDistance < dist[v.vertexLabel]) { // at first dist[v.vertexLabel] has infinity
                    dist[v.vertexLabel] = newDistance;
                }
                //System.out.println("vertexLabel=" + v.vertexLabel + "    Distance=" + dist[v.vertexLabel]);
                // Add the current vertex to the PriorityQueue 
                pqueue.add(new Node(v.vertexLabel, dist[v.vertexLabel]));
                //System.out.println("size of queue: " + pqueue.size());
                

            }
        }
    }

    void dijkstraSP(Dijkstra dpq, int source) {
        System.out.println("Dijkstra Algorithm: ");
        System.out.println("Source: " + source);
        System.out.println("The shorted path from source node to other nodes:");
        System.out.println("Source\t\t" + "Node#\t\t" + "Shortest Path");
        for (int i = 0; i < dpq.dist.length; i++) {
            System.out.println(source + " \t\t " + i + " \t\t " + dpq.dist[i]);
        }
    }

}
//used to store every adjacent vertex with its corresponding weight and label

class Node implements Comparator<Node> {

    public int vertexLabel;
    public int weight;

    public Node() {
    } //empty constructor 

    public Node(int node, int weight) {
        this.vertexLabel = node;
        this.weight = weight;
    }

    @Override
    public int compare(Node node1, Node node2) {
        if (node1.weight < node2.weight) {
            return -1;
        }
        if (node1.weight > node2.weight) {
            return 1;
        }
        return 0;
    }
}

//create the primpq
class Prim {

    int noOfVertices;
    List<List<Node>> adj;//TO STORE EVERY VERTEX WITH ITS ADJACENTS

    public Prim(int vertices) {

        this.noOfVertices = vertices;
        adj = new ArrayList<>();
        for (int i = 0; i < vertices; i++) {
            adj.add(new ArrayList<>());
        }
    }

    void addEdge(int u, int v, int w) {//takes 2 vertex and weight between them

        adj.get(u).add(new Node(v, w));//if A is connected to B
        adj.get(v).add(new Node(u, w));//B must be connected to A
    }

    void primMST() {
        PriorityQueue<Node> queue = new PriorityQueue<>(noOfVertices, new Comparator<Node>() {
            public int compare(Node a, Node b)//used when add,poll,peek
            {
                return a.weight - b.weight;//-ve A comes before B//+ve B should come before A
            }
        });
        int source = 0;
        int defaultKey = Integer.MAX_VALUE;//in the beginning
        int[] keyValues = new int[noOfVertices];
        Arrays.fill(keyValues, defaultKey);
        // To store parent array which in turn store MST
        int[] parent = new int[noOfVertices];//store parent of each vertex in MST
        Arrays.fill(parent, -1);

        // To keep track of vertices included in MST
        boolean[] inMST = new boolean[noOfVertices];
        // Insert source itself in priority queue and
        // initialize its key as 0.
        queue.offer(new Node(0, source));
        keyValues[source] = 0;//awel vertex lessa lwa7daha f edgeWeight=0
        while (!queue.isEmpty())//continues until all vertices have been added to MST
        {
            int u = queue.peek().weight;//get the vertex with smallest key value
            queue.poll();//remove this vertex from queue because it will be added to MST
            if (inMST[u]) {
                continue;
            }
            inMST[u] = true;//include this vertex in MST
            for (Node node : adj.get(u)) {

                // getting all adjacents of u.
                int v = node.vertexLabel;
                int weight = node.weight;

                //  If v is not in MST and weight of (u,v)
                //  is smaller
                // than defaultkey of v
                if (!inMST[v] && keyValues[v] > weight) {
                    // Updating key of v
                    keyValues[v] = weight;
                    queue.offer(new Node(keyValues[v], v));
                    parent[v] = u;
                }
            }
        }
// Print edges of MST using parent array
        System.out.println("Prim Algorithm: ");
        for (int i = 1; i < noOfVertices; i++) {
            System.out.println(parent[i] + " - " + i);
        }
    }
}
