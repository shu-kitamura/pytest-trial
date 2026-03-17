# テストのスキップ方法

特定のテストをスキップしたいときの方法

## 必ずスキップする

テストの前に `@pytest.mark.skip` を付けることで、必ずスキップできる。  

```python
@pytest.mark.skip(reason="Test not implemented yet")
def test_skip():
    assert ...
```



## 条件を満たしたときにスキップする

テストの前に `@pytest.mark.skipif(条件)` を付けることで、条件を満たした場合のみスキップできる。  

```python
@pytest.mark.skipif(sys.platform != "linux" ,reason="Test not implemented yet")
def test_skip_linux():
    assert ...

@pytest.mark.skipif(sys.platform != "win32" ,reason="Test not implemented yet")
def test_skip_windows():
    assert ...
```

## テストの中でスキップを判定する

テストの中で `pytest.skip()` を実行することでテストをスキップできる。  
skipif の条件が複雑な場合などはこちらを使った方がいいような気がする。  

```python
def test_skip_in_method():
    if True:
        pytest.skip("Skipping this test because of some condition")

    assert ...
```
