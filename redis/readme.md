## Инструкция по установке Redis на macOS

- Для установки требуется https://brew.sh/
  `brew install redis`
- для запуска сервиса
  `brew services start redis`
- для остановки
  `brew services stop redis`
- для удаления
  `brew uninstall redis`

## Инструкция по установке Redis на Windows

- Действуем по инструкции с официального сайта проекта Chocolatey.
```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
- Находим в поиске Chocolatey нужный пакет Redis, например, https://chocolatey.org/packages/redis-64/3.0.503
- Устанавливаем:
```shell
choco install redis-64 --version 3.0.503
```
- Запускаем redis server и redis cli:
```shell
redis-server
```
```shell
redis-cli
```

## Запуск в docker

Выполните в терминале следующую команду (в одну строчку):
```shell
docker run --rm --name redis -p 127.0.0.1:6379:6379/tcp -d redis
```

Чтобы подключиться используя клиент командной строки, наберите команду (в одну строчку):

```shell
docker exec -it redis redis-cli -a redispw
```
