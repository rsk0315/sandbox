(
  r'(?:foo)+(bar)*[baz]?[^qux]+?'
  r'.^$'
  r'quux{2,3}'
  r'corge{2}'
  r'grault{,4}'
  r'\\\.\^\$\*\+\?\{\x00\u0000\U00000000\x[]'
  ur'\x0\x00\u0000\U00000000\N{LATIN SMALL LETTER A}'
  r'|(?iLmsuxc)(?P<NAME>...)(?P=NAME)(?#COMMENT)'
  r'(?=a)(?!b)(?<=c)(?<!d)(?(id)yes|no)\A\Z\b\B\g<1>\2\D\w\x\y\z'
)
'\x00\u0000\U00000000'
