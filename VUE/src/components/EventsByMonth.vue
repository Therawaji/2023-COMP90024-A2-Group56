<template>
    <div>
        <div ref="chart" style="height: 500px;"></div>
        <ul>{{string}}</ul>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string: 'nothing',
            chart: null,
            chartData: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/events/by_month');
                console.log(response.data);
                this.chartData = response.data;
                this.updateChart();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart() {
            this.chart.setOption(
                {
                  title: {
                    text: 'Genre by Month'
                  },
                  tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                      type: 'shadow'
                    }
                  },
                  legend: {},
                  grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                  },
                  xAxis: {
                    type: 'value',
                    boundaryGap: [0, 0.01]
                  },
                  yAxis: {
                    type: 'category',
                    data: ['Brisbane', 'Melbourne', 'Sydney']
                  },
                  series: [
                    {
                      name: this.chartData[0][0],
                      type: 'bar',
                      data: this.chartData[0][1]
                    },
                    {
                      name: this.chartData[1][0],
                      type: 'bar',
                      data: this.chartData[1][1]
                    },
                    {
                      name: this.chartData[2][0],
                      type: 'bar',
                      data: this.chartData[2][1]
                    },
                    {
                      name: this.chartData[3][0],
                      type: 'bar',
                      data: this.chartData[3][1]
                    },
                    {
                      name: this.chartData[4][0],
                      type: 'bar',
                      data: this.chartData[4][1]
                    },
                    {
                      name: this.chartData[5][0],
                      type: 'bar',
                      data: this.chartData[5][1]
                    },
                    {
                      name: this.chartData[6][0],
                      type: 'bar',
                      data: this.chartData[6][1]
                    }
                  ]
                }
            );
        },
    },
    mounted() {
        this.chart = echarts.init(this.$refs.chart);
        this.getData1();
    },
}
</script>
