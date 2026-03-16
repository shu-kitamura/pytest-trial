# pytest で型ヒントを使う理由

## Why type tests?

- **Readability**  
  期待される入出力を明確に定義することで、複雑なテストの可読性を向上させる。

- **Refactoring**
  アプリケーションのコードを変更したとき、型チェッカーによって、テストを実行する前に検査できる。  

型を使うことで、可読性が高く、メンテナンスしやすいテストを書ける。

## fixture で型をつける  

fixture 側では、通常の関数と同様に型を追加する
```diff
import pytest

@pytest.fixture
-def sample_fixture():
+def sample_fixture() -> int:
    return 38
```

テスト関数では、fixture を受け取る引数に型注釈をつける

```diff
-def test_sample_fixture(sample_fixture):
+def test_sample_fixture(sample_fixture: int) -> None:
    assert sample_fixture == 38
```

## parametrize に型をつける

parametrize に型を使う場合も、テスト関数では受け取る引数に型注釈をつける

```diff
@pytest.mark.parametrize("input_value, expected_output", [(1, 2), (5, 6), (10, 11)])
-def test_increment(input_value, expected_output):
+def test_increment(input_value: int, expected_output: int) -> None:
    assert input_value + 1 == expected_output
```