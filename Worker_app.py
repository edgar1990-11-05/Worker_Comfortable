<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Рабочий Трекер</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { -webkit-tap-highlight-color: transparent; }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="bg-gray-100 min-h-screen p-4 font-sans">
    <div class="max-w-md mx-auto bg-white rounded-2xl shadow-xl p-6">
        <h1 class="text-2xl font-bold text-center mb-6 text-blue-600">Worker Comfortable</h1>
        
        <div class="grid grid-cols-2 gap-4 mb-6">
            <div>
                <label class="block text-sm font-medium text-gray-700">Ставка €/ч</label>
                <input type="number" id="rate_n" value="10" class="w-full mt-1 p-3 border rounded-xl focus:ring-2 focus:ring-blue-500 outline-none">
            </div>
            <div>
                <label class="block text-sm font-medium text-gray-700">Сверх €/ч</label>
                <input type="number" id="rate_o" value="15" class="w-full mt-1 p-3 border rounded-xl focus:ring-2 focus:ring-blue-500 outline-none">
            </div>
        </div>

        <div id="days-container" class="space-y-4 mb-6 max-h-[50vh] overflow-y-auto no-scrollbar">
            </div>

        <button onclick="addDay()" class="w-full bg-blue-500 text-white py-4 rounded-xl font-bold text-lg active:scale-95 transition-transform mb-4">
            + Добавить день
        </button>

        <div class="bg-blue-50 p-4 rounded-xl border-2 border-blue-100">
            <div class="flex justify-between items-center mb-2">
                <span class="text-gray-600">Всего часов:</span>
                <span id="total-hours" class="font-bold text-xl">0.00</span>
            </div>
            <div class="flex justify-between items-center text-blue-700">
                <span class="text-lg">К ОПЛАТЕ:</span>
                <span id="total-pay" class="font-black text-2xl">0.00 €</span>
            </div>
        </div>
    </div>

    <script>
        let dayCount = 0;

        function addDay() {
            dayCount++;
            const container = document.getElementById('days-container');
            const dayHtml = `
                <div class="bg-gray-50 p-4 rounded-xl border border-gray-200 animate-in fade-in duration-300">
                    <div class="flex justify-between mb-2 items-center">
                        <span class="font-bold text-gray-700">День ${dayCount}</span>
                        <input type="number" placeholder="Обед (мин)" class="w-20 p-1 text-sm border rounded" oninput="calculate()">
                    </div>
                    <div class="flex gap-2">
                        <input type="time" value="07:00" class="flex-1 p-2 border rounded-lg" oninput="calculate()">
                        <input type="time" value="16:00" class="flex-1 p-2 border rounded-lg" oninput="calculate()">
                    </div>
                </div>
            `;
            container.insertAdjacentHTML('beforeend', dayHtml);
            calculate();
        }

        function calculate() {
            let totalH = 0;
            const rateN = parseFloat(document.getElementById('rate_n').value) || 0;
            const rateO = parseFloat(document.getElementById('rate_o').value) || 0;
            let totalMoney = 0;

            const days = document.querySelectorAll('#days-container > div');
            days.forEach(day => {
                const inputs = day.querySelectorAll('input');
                const breakMin = parseFloat(inputs[0].value) || 0;
                const start = inputs[1].value;
                const end = inputs[2].value;

                if(start && end) {
                    const s = new Date('2024-01-01T' + start);
                    const e = new Date('2024-01-01T' + end);
                    let diff = (e - s) / 1000 / 3600;
                    if(diff < 0) diff += 24;
                    
                    const net = Math.max(0, diff - (breakMin / 60));
                    totalH += net;

                    if(net > 8) {
                        totalMoney += (8 * rateN) + ((net - 8) * rateO);
                    } else {
                        totalMoney += net * rateN;
                    }
                }
            });

            document.getElementById('total-hours').innerText = totalH.toFixed(2);
            document.getElementById('total-pay').innerText = totalMoney.toFixed(2) + ' €';
        }

        // Добавим первый день сразу
        addDay();
    </script>
</body>
</html>
