# VOICEROIDpy

## Description
pythonから民安★TALKへの橋渡し

## Requirement
- 民安★TALK
- VOICEROID

## Useage
vrx_pathに民安★TALKのpathを渡す
```python
import voiceroid as v

vrx_path = "E:\\Users\\Sakurai\\Archives\\Apps\\tamiyasu_talk\\vrx.exe"
yukari = v.Voiceroid(vrx_path)

yukari.talk("テスト")
```

