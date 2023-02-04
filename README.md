# 😊 `dimples`
_Distribute and manage your Python packages with `dimples`!_

## Vision

### Command Line
```bash
python -m pip install --upgrade dimples

python -m dimples generate my-new-package
python -m dimples activate my-new-package
python -m dimples add numpy
python -m dimples status

python -m dimples activate 
```

### Python
```python
import dimples as dmp

dmp.generate("my-new-package")
dmp.activate("my-new-package")

dmp.add("numpy")
dmp.status()

dmp.activate()

```
## Notes

### The Path of the Crab

- https://doc.rust-lang.org/cargo/reference/registries.html

### Indirect Dependencies With Same Name

- https://pkgdocs.julialang.org/v1/toml-files/#Multiple-package-with-the-same-name

