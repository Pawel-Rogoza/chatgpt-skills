# A0 — pakowanie i zakres prób

Baza: `aa0793263e8e936f0a08d7b49c9a6c9f96658163`, PR #1 otwarty i niescalony podczas sprawdzenia przez GitHub 23.09.2026. A0 nie zmienia wersji ani treści instalowanego pluginu 0.1.0; zmienia narzędzie budowania.

15 testów technicznych przechodzi lokalnie. Obejmują dotychczasowe granice i nową konfigurację: trzeci skill z dwiema własnymi referencjami oraz jednym wspólnym plikiem, wadliwe i powtórzone wpisy, brak konfiguracji, kolizje ścieżek, symlinki plików/katalogów/źródeł, dokładną zawartość ZIP i reprodukowalność. `check` potwierdził 15 plików. Wspólne referencje i instrukcje dwóch istniejących skilli pozostają bez zmian.

[Trzy odpowiedzi własne](a0-self-check.md) pokrywają korektę językową, poprawny fragment pisma i wąską poprawkę z argumentem alternatywnym. Są znane implementatorowi i ocenione przez niego, więc nie dowodzą niezależnej jakości ani przewagi nad baseline. **Routing hosta: niesprawdzony.** Nie oznaczamy statycznej kontroli listy triggerów jako testu automatycznego uruchomienia.

Konfigurację opisano w [instrukcji](../../../docs/package-configuration.md). Identyfikatora `personal` nie zmieniono; przed instalacją w innym środowisku nadal trzeba sprawdzić jego źródło. W tym etapie nie wykonywano instalacji ani publikacji.
