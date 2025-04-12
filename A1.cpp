
#include <iostream>
using namespace std;

class Graph
{
private:
    int adjMatrix[50][50];
    int vertices;

public:
    Graph(int v)
    {
        vertices = v;
        for (int i = 0; i < v; i++)
        {
            for (int j = 0; j < v; j++)
            {
                adjMatrix[i][j] = 0;
            }
        }
    }

    void addEdge(int u, int v)
    {
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1;
    }

    void DFS(int start, bool visited[])
    {
        visited[start] = true;
        cout << start << " ";

        for (int i = 0; i < vertices; i++)
        {
            if (adjMatrix[start][i] == 1 && !visited[i])
            {
                DFS(i, visited);
            }
        }
    }
    void DFSUtil(int start)
    {
        bool visited[50];
        for (int i = 0; i < vertices; i++)
        {
            visited[i] = false;
        }

        cout << "DFS Traversal: ";
        DFS(start, visited);
        cout << endl;
    }

    void BFS(int start)
    {
        bool visited[50];
        int queue[50];
        int front = 0, rear = 0;

        for (int i = 0; i < vertices; i++)
        {
            visited[i] = false;
        }

        visited[start] = true;
        queue[rear++] = start;

        cout << "BFS Traversal: ";
        while (front < rear)
        {
            int current = queue[front++];
            cout << current << " ";

            for (int i = 0; i < vertices; i++)
            {
                if (adjMatrix[current][i] == 1 && !visited[i])
                {
                    visited[i] = true;
                    queue[rear++] = i;
                }
            }
        }
        cout << endl;
    }
};

int main()
{
    Graph g(7);

    g.addEdge(1, 3);
    g.addEdge(1, 5);
    g.addEdge(1, 4);
    g.addEdge(3, 5);
    g.addEdge(2, 5);
    g.addEdge(5, 6);

    g.DFSUtil(1);
    g.BFS(1);

    return 0;
}