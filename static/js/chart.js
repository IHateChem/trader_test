// 데이터 파싱
var data = JSON.parse('{{  data_json }}');

// 그래프 설정
var chart = c3.generate({
    bindto: '#chart',
    data: {
        json: data,
        keys: {
            x: 'Epoch',
            value: ['#Buy', '#Sell', '#Hold']
        },
        type: 'line'
    },
    axis: {
        x: {
            label: 'Epoch'
        },
        y: {
            label: 'Count'
        }
    },
    legend: {
        position: 'right'
    }
});
