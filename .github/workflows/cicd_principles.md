## Yleiset periaatteet

### **Separation of Concerns**
- **ci.yml:** Koodin laatu
- **manual.yml:** Operaatiot
- **deploy.yml:** Julkaisu

### **Security Principle**
```yaml
# Hyvä - rajoitettu trigger
on:
  push:
    branches: [main]

# Huono - liian laaja
on: [push, pull_request]
```

### **Caching Strategy**
```yaml
# Dependencies cache
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: .venv
    key: ${{ runner.os }}-deps-${{ hashFiles('**/pyproject.toml') }}

# Build cache
- name: Cache build
  uses: actions/cache@v4
  with:
    path: build/
    key: ${{ runner.os }}-build-${{ github.sha }}
```

### **Environment Variables**
```yaml
env:
  PYTHON_VERSION: '3.13'
  DOCKER_REGISTRY: 'gcr.io/your-project'

jobs:
  test:
    env:
      DATABASE_URL: ${{ secrets.TEST_DB_URL }}
```

**Miksi tämä rakenne?**
1. **Modularity:** Jokainen workflow on erillinen
2. **Maintainability:** Helppo muuttaa yhtä osaa
3. **Security:** Eri oikeudet eri workflow:ille
4. **Performance:** Caching optimoitu per workflow

Haluatko että rakennamme jonkin näistä workflow:ista yhdessä? Vai onko jotain epäselvää periaatteista? 🤔
        