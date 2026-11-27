# Command
``` bash
mkdir -p tuan-09 && { printf '# Run Log 3x - Tuan 09\n'; for i in 1 2 3; do printf '\n## Lan chay %d (%s)\n```text\n' "$i" "$(date '+%Y-%m-%d %H:%M:%S')"; pytest -v tuan-05 tuan-07 tuan-08 2>&1; printf '```\n'; done; } | tee tuan-09/run_log.md
```

# Run Log 3x - Tuan 09

## Lan chay 1 (2026-11-27 06:55:48)
```text
============================= test session starts ==============================
platform linux -- Python 3.14.2, pytest-9.2.0, pluggy-1.7.0 -- /usr/local/py-utils/venvs/pytest/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/kttd-C06-N08
plugins: platformdirs-4.14.0, anyio-4.15.1
collecting ... collected 12 items

tuan-05/test_login.py::test_login_valid_credentials PASSED               [  8%]
tuan-05/test_login.py::test_login_invalid_password PASSED                [ 16%]
tuan-05/test_login.py::test_login_invalid_username PASSED                [ 25%]
tuan-05/test_login.py::test_login_empty_credentials PASSED               [ 33%]
tuan-05/test_login.py::test_login_empty_password PASSED                  [ 41%]
tuan-07/test_checkboxes.py::test_checkboxes_fail_case_invalid_action PASSED [ 50%]
tuan-07/test_checkboxes.py::test_checkbox_happy_path PASSED              [ 58%]
tuan-07/test_checkboxes.py::test_checkbox_not_persisted_after_refresh PASSED [ 66%]
tuan-08/test_upload.py::test_upload_file_invalid PASSED                  [ 75%]
tuan-08/test_upload.py::test_upload_invalid_file_fail_case XFAIL (Ap...) [ 83%]
tuan-08/test_upload.py::test_upload_valid_file PASSED                    [ 91%]
tuan-08/test_upload.py::test_upload_empty_file XFAIL (App bug: /uplo...) [100%]

======================== 10 passed, 2 xfailed in 48.84s ========================
```

## Lan chay 2 (2026-11-27 06:56:38)
```text
============================= test session starts ==============================
platform linux -- Python 3.14.2, pytest-9.2.0, pluggy-1.7.0 -- /usr/local/py-utils/venvs/pytest/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/kttd-C06-N08
plugins: platformdirs-4.14.0, anyio-4.15.1
collecting ... collected 12 items

tuan-05/test_login.py::test_login_valid_credentials PASSED               [  8%]
tuan-05/test_login.py::test_login_invalid_password PASSED                [ 16%]
tuan-05/test_login.py::test_login_invalid_username PASSED                [ 25%]
tuan-05/test_login.py::test_login_empty_credentials PASSED               [ 33%]
tuan-05/test_login.py::test_login_empty_password PASSED                  [ 41%]
tuan-07/test_checkboxes.py::test_checkboxes_fail_case_invalid_action PASSED [ 50%]
tuan-07/test_checkboxes.py::test_checkbox_happy_path PASSED              [ 58%]
tuan-07/test_checkboxes.py::test_checkbox_not_persisted_after_refresh PASSED [ 66%]
tuan-08/test_upload.py::test_upload_file_invalid PASSED                  [ 75%]
tuan-08/test_upload.py::test_upload_invalid_file_fail_case XFAIL (Ap...) [ 83%]
tuan-08/test_upload.py::test_upload_valid_file PASSED                    [ 91%]
tuan-08/test_upload.py::test_upload_empty_file XFAIL (App bug: /uplo...) [100%]

======================== 10 passed, 2 xfailed in 48.92s ========================
```

## Lan chay 3 (2026-11-27 06:57:28)
```text
============================= test session starts ==============================
platform linux -- Python 3.14.2, pytest-9.2.0, pluggy-1.7.0 -- /usr/local/py-utils/venvs/pytest/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/kttd-C06-N08
plugins: platformdirs-4.14.0, anyio-4.15.1
collecting ... collected 12 items

tuan-05/test_login.py::test_login_valid_credentials PASSED               [  8%]
tuan-05/test_login.py::test_login_invalid_password PASSED                [ 16%]
tuan-05/test_login.py::test_login_invalid_username PASSED                [ 25%]
tuan-05/test_login.py::test_login_empty_credentials PASSED               [ 33%]
tuan-05/test_login.py::test_login_empty_password PASSED                  [ 41%]
tuan-07/test_checkboxes.py::test_checkboxes_fail_case_invalid_action PASSED [ 50%]
tuan-07/test_checkboxes.py::test_checkbox_happy_path PASSED              [ 58%]
tuan-07/test_checkboxes.py::test_checkbox_not_persisted_after_refresh PASSED [ 66%]
tuan-08/test_upload.py::test_upload_file_invalid PASSED                  [ 75%]
tuan-08/test_upload.py::test_upload_invalid_file_fail_case XFAIL (Ap...) [ 83%]
tuan-08/test_upload.py::test_upload_valid_file PASSED                    [ 91%]
tuan-08/test_upload.py::test_upload_empty_file XFAIL (App bug: /uplo...) [100%]

======================== 10 passed, 2 xfailed in 49.07s ========================
```
