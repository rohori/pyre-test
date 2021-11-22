from typing import Callable, Dict, Iterable, List, Optional, Tuple, TypeVar, Union

K = TypeVar("K")
V = TypeVar("V")
R = TypeVar("R")
F = TypeVar("F")
S = TypeVar("S")

def vmap(f: Callable[[V], R], d: Dict[K, V]) -> Dict[K, R]:
    """map over dict values."""
    return {k: f(v) for (k, v) in d.items()}

def first(t: Tuple[F, S]) -> F:
    """First item of 2-tuple."""
    return t[0]

a: Dict[str, Tuple[str, int]] = {"en": ("hello", 5), "ja": ("こんにちは", 5)}
print(a)
print(vmap(first, a))
