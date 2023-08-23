Voight-Kampff test
==================
Перед вами моя имплементация [теста Войта-Кампфа](https://bladerunner.fandom.com/wiki/Voight-Kampff_test) из к/ф "Бегущий по лезвию".  
Этот тест был создан для определения так называемых "репликантов". Делал он это посредством эмоционально провокационных вопросов и постоянного замера таких показателей как:
- Частота дыхания
- Частота сердечных сокращений
- Уровень покраснения
- Ширина зрачков

## Процесс тестирования
Всего 10 вопросов. Каждый имеет четыре варианта ответа, выбрать можно только один.  
После каждого ответа необходимо ввести показатели состояния испытуемого.  
В конце будет автоматически проведена проверка и выдан результат.  
Чтобы начать склонируйте репозиторий и введите `python main.py`

>[!NOTE]
>Для удобства была введена возможность пропустить вопросы и сбор анамнеза.
>Нажимаем Enter, будут введены рандомные ответы

## Цель проекта
Знакомство с возможностями Pytest и Sphinx.  
По завершению теста Pytest автоматически предоставляет полный отчет о тестировании.
Сгенерированную Sphinx документацию можно найти в `/docs/build/html/index.html`
