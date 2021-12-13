import dec12


class TestDec12:
    def test_read_data(self):
        data = dec12.get_data(toy=True)
        assert data[0] == ["start", "A"]

    def test_get_graph(self):
        data = dec12.get_data(toy=True)
        graph = dec12.get_graph(data)
        assert graph.number_of_edges() == 7

    def test_get_paths(self):
        data = dec12.get_data(toy=True)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths(graph, start="start", end="end")
        assert len(list(paths)) == 10

    def test_get_paths_toy(self):
        data = dec12.get_data(toy=True)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths(graph, start="start", end="end")
        assert len(list(paths)) == 10

    def test_get_paths_megatoy(self):
        data = dec12.get_data(toy=True, mega=True)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths(graph, start="start", end="end")
        assert len(list(paths)) == 226

    def test_get_paths_real(self):
        data = dec12.get_data(toy=False)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths(graph, start="start", end="end")
        assert len(list(paths)) == 3000

    def test_get_paths_revisit_small_toy(self):
        data = dec12.get_data(toy=True)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths_revisit_small(graph, start="start", end="end")
        assert len(list(paths)) == 36

    def test_get_paths_revisit_small_megatoy(self):
        data = dec12.get_data(toy=True, mega=True)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths_revisit_small(graph, start="start", end="end")
        assert len(list(paths)) == 3509

    def test_get_paths_revisit_small_real(self):
        data = dec12.get_data(toy=False)
        graph = dec12.get_graph(data)
        paths = dec12.get_paths_revisit_small(graph, start="start", end="end")
        assert len(list(paths)) == 74222
