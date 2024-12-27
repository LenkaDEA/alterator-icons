# Спецификация значков

Для соответствия общему стилю значков приложений альтератора иконки должны быть выполнены с учетом следующих рекомендаций:
1. Значки выполняются в одном цвете для:
- светлой темы: #232629
- темной темы: #D8D8D8
2. Толщина линий 1px
3. В .svg файле необходимо прописать следущие параметры в начале: `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="none" viewBox="0 0 32 32">`,
где viewBox - необходим для корректного отображения необходимого размера.
*в Figma можно использовать плагин SVG Export для корректного экспорта значков*
4. Для корректного масштабирования каждый значок должен быть реализован в 3 размерах: 16x16, 22x22, 32x32.

### Схема наименования значков
| icon                                                                              | alterator-theme       | theme name            |
| --------------------------------------------------------------------------------- | --------------------- | --------------------- |
| ![go-previous](alterator-icons/alterator/16x16/go-previous.svg)                   | go-previous           | go-previous           |
| ![go-next](alterator-icons/alterator/16x16/go-next.svg)                           | go-next               | go-next               |
| ![media-playback-stop](alterator-icons/alterator/16x16/media-playback-stop.svg)   | media-playback-stop   | media-playback-stop   |
| ![media-playback-start](alterator-icons/alterator/16x16/media-playback-start.svg) | media-playback-start  | media-playback-start  |
| ![document-revert](alterator-icons/alterator/16x16/document-revert.svg)           | document-revert       | document-revert       |
| ![text-x-log](alterator-icons/alterator/16x16/text-x-log.svg)                     | text-x-log            | text-x-log            |
| ![process-stop](alterator-icons/alterator/16x16/process-stop.svg)                 | process-stop          | process-stop          |
| ![system-run](alterator-icons/alterator/16x16/system-run.svg)                     | system-run            | system-run            |
| ![preferences-other](alterator-icons/alterator/16x16/preferences-other.svg)       | preferences-other     | preferences-other     |
| ![dialog-ok-apply](alterator-icons/alterator/16x16/dialog-ok-apply.svg)           | dialog-ok-apply       | dialog-ok-apply       |
| ![dialog-close](alterator-icons/alterator/16x16/dialog-close.svg)                 | dialog-close          | dialog-close          |
| ![text-x-log](alterator-icons/alterator/16x16/text-x-log.svg)                     | text-x-log            | text-x-log            |

Названия значков должны соответствовать названиям подобных значков в общих системных темах, если они заменяют их. Если же в системных темах нет подобного значка, то название можно придумать свое, отражающее то, что изображено на значке. (несколько слов в названии пишутся через "-").


## Советы по реализации значков в Figma
Важно перед экспортом готового значка его "запечь", применив функцию outline stroke, которая преобразует линии в законченные фигуры. Это свойство очень важно для корректного отображения значка в системе.

Линии и элементы должны попадать в пиксели фрейма, для четкого отображения на мониторах.

Разные размеры значков (16x16,22x22,32x32) используются для корректного масштабирования. Например, если линию 1px значка размера 16x16 увеличить до размера 32x32, то линия в 1px станет 2px.

*Это свойство можно также регулировать параметрами svg файла, но в данном случае было принято решение использовать разные размеры по аналогии с системными темами значков.*